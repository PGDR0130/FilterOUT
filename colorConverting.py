# Converting Different Color Types

def hexToRGB(hex):
  rgb = []
  for i in (0, 2, 4):
    decimal = int(hex[i:i+2], 16)
    rgb.append(decimal)
  return tuple(rgb)

def RGBToHex(r, g, b):
  return '#%02X%02X%02X' % (r, g, b)

