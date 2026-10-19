def linearize(channel):
    s = channel / 255
    if s <= 0.03928:
        return s / 12.92
    else:
        return ((s + 0.055) / 1.055) ** 2.4


def relative_luminance(color):
    r, g, b = color
    return 0.2126 * linearize(r) + 0.7152 * linearize(g) + 0.0722 * linearize(
        b)


def contrast_ratio(color_a, color_b):
    lum_a = relative_luminance(color_a)
    lum_b = relative_luminance(color_b)
    lighter = max(lum_a, lum_b)
    darker = min(lum_a, lum_b)
    return (lighter + 0.05) / (darker + 0.05)


if __name__ == "__main__":
    print(contrast_ratio((0, 0, 0), (255, 255, 255)))
    print(contrast_ratio((255, 255, 255), (255, 255, 255)))
    print(contrast_ratio((0, 0, 255), (0, 0, 0)))