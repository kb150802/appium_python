def swipe_left(element ,driver):
    x_coordinate, y_coordinate = element.location['x'], element.location['y']
    size = element.size
    height, width = size['height'], size['width']
    start_x = x_coordinate + width // 2
    end_x = 0
    start_y = y_coordinate + height // 2
    driver.swipe(start_x, start_y, end_x, start_y, 400)
    return

def swipe_right(element, driver):
    x_coordinate, y_coordinate = element.location['x'], element.location['y']
    size = element.size
    height, width = size['height'], size['width']
    end_x = x_coordinate + width
    start_x = x_coordinate + width // 2
    start_y = y_coordinate + height // 2
    driver.swipe(start_x, start_y, end_x, start_y, 400)
    return