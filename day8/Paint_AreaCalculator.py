
# Calculate the area of a rectangle for painting coverage
def paint_calc(height, width, cover):
    result = round((height + width) / cover)
    print(f"You'll need {result} of paint.)")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)