"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be balanced in criticality if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    if temperature < 800 and neutrons_emitted > 500 and temperature*neutrons_emitted < 500000:
        return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percentage_value = (generated_power/ theoretical_max_power)*100
    if percentage_value >= 80:
        return f"green"
    elif percentage_value >= 60 and percentage_value < 80:
        return f"orange"
    elif percentage_value >= 30 and percentage_value < 60:
        return f"red"
    elif percentage_value < 30:
        return f"black"
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    maths = temperature * neutrons_produced_per_second
    calculation = 0.9*threshold
    if maths < calculation :
        return f'LOW'
    elif maths <= 1.1 * threshold:
        return f'NORMAL'
    else:
        return f'DANGER'