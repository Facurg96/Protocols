import math
from opentrons.types import Point

metadata = {
    'protocolName': 'Agriseq Library Prep Part 1 - DNA transfer (96)',
    'author': 'Rami Farawi <rami.farawi@opentrons.com>',
    'source': 'Custom Protocol Request',
    'apiLevel': '2.11'
}


def run(protocol):

    [num_samp, m20_mount] = get_values(  # noqa: F821
        "num_samp", "m20_mount")

    if not 1 <= num_samp <= 288:
        raise Exception("Enter a sample number between 1-288")

    num_col = math.ceil(num_samp/8)
    tip_counter = 0

    # load labware
    sample_plates = [protocol.load_labware(
                    'fisherscientific_96_wellplate_200ul',
                     str(slot), label='Sample Plate') for slot in [1, 2, 3]]
    reaction_plates = [protocol.load_labware('customendura_96_wellplate_200ul',
                       str(slot), label='Reaction Plate')
                       for slot in [4, 5, 6]]
    mmx_plate = protocol.load_labware('customendura_96_wellplate_200ul', '7',
                                      label='MMX Plate')
    tiprack20 = [protocol.load_labware('opentrons_96_filtertiprack_20ul',
                                       str(slot))
                 for slot in [8, 9, 10, 11]]

    # load instruments
    m20 = protocol.load_instrument('p20_multi_gen2', m20_mount,
                                   tip_racks=tiprack20)

    tips = [col for tipbox in tiprack20 for col in tipbox.rows()[0]]

    def touchtip(pip, well):
        knock_loc = well.top(z=-1).move(
                    Point(x=-(well.diameter/2.25)))
        knock_loc2 = well.top(z=-1).move(
                Point(x=(well.diameter/2.25)))
        pip.move_to(knock_loc)
        pip.move_to(knock_loc2)

    def pick_up():
        nonlocal tip_counter
        if tip_counter == 36:
            protocol.home()
            protocol.pause('Replace 20 ul tip racks on Slots 9, 10, and 11')
            m20.reset_tipracks()
            tip_counter = 0
            pick_up()
        else:
            m20.pick_up_tip(tips[tip_counter])
            tip_counter += 1

    sample_plate_cols = [col for plate in sample_plates
                         for col in plate.rows()[0]][:num_col]
    reaction_plate_cols = [col for plate in reaction_plates
                           for col in plate.rows()[0]][:num_col]

    # load reagents
    amplify_mix = mmx_plate.rows()[0][0]

    # add amplification mix
    airgap = 2
    pick_up()
    for col in reaction_plate_cols:
        m20.aspirate(7, amplify_mix)
        touchtip(m20, amplify_mix)
        m20.air_gap(airgap)
        m20.dispense(airgap, col.top())
        m20.dispense(7, col)
        m20.blow_out()
        touchtip(m20, col)
    m20.return_tip()

    # add DNA
    for s, d in zip(sample_plate_cols, reaction_plate_cols):
        pick_up()
        m20.aspirate(3, s)
        touchtip(m20, s)
        m20.air_gap(airgap)
        m20.dispense(airgap, d.top())
        m20.dispense(3, d)
        m20.mix(2, 5, d)
        m20.blow_out()
        touchtip(m20, d)
        m20.return_tip()

    protocol.home()
    protocol.pause('''Protocol method complete. Please remove reaction plates
                   from deck and proceed with PCR and centrifuge steps.
                   Return reaction plates back to deck and continue to
                   Part 2 - Pre-ligation.''')
