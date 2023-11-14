# takes in a line length and returns the points for that line

def GET_points(length: int) -> int:
    points = [1, 2, 4, 7]
    return(points[length])

def nameLines(row):
    return f'{row[0][:2]}{row[1][:2]}{row[2][:2]}{row[3]}'