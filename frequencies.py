FREQUENCY_MAP = {
    "monthly": 12,
    "quarterly": 4,
    "semi_annual": 2,
    "annual": 1,
}

def parse_frequency(freq_str: str) -> int:
    freq_str = freq_str.lower().replace("-", "_")  
    if freq_str not in FREQUENCY_MAP:
        raise ValueError(f"Unknown frequency: {freq_str}")
    return FREQUENCY_MAP[freq_str]
