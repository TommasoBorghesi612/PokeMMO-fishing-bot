import pyautogui
from PIL import Image, ImageChops
import numpy as np
import time
import random

ref_images_keys = ['male_1', 'male_10', 'nibble', 'landed', 'end_balls']
reference_images_path = ['images/male_1_symbol.png', 'images/male_10_symbol.png', 'images/nibble_symbol.png', 'images/landed_symbol.png', 'images/end_balls_symbol.png']

def calculate_difference(image1, image2):
    """
    Calculate the difference between two images and find the most significant change.
    :param image1: PIL image object (screenshot).
    :param image2: PIL image object (reference image).
    :return: Tuple (x, y) indicating the point of maximum difference.
    """
    # Convert images to numpy arrays
    array1 = np.array(image1)
    array2 = np.array(image2)
    
    # Compute absolute difference
    diff = np.abs(array1.astype('int') - array2.astype('int'))
    diff_sum = np.sum(diff)/(diff.shape[0] * diff.shape[1] * diff.shape[2])  # Combine RGB channels

    return diff_sum

def move_mouse_to_point(x, y):
    """
    Move the mouse to a specified point on the screen.
    :param x: X-coordinate.
    :param y: Y-coordinate.
    """
    pyautogui.moveTo(x, y)

def main():
    
    pointer_coordinates = {
        'rod' : (653, 49),
        'ball' : (400, 700),
        'rock' : (400, 760),
        'baloon' : (1363, 195),
        'close_window' : (1194, 392),
        'run' : (610, 760),
        'safari_start' : (960, 770)
    }

    ref_images_coords = {
        'male_1' : (454, 153, 9, 15),
        'male_10' : (463, 153, 9, 15),
        'nibble' : (689, 141, 95, 21),
        'landed' : (671, 138, 119, 24),
        'end_balls' : (560, 141, 170, 26)
    }
    
    max_diff = 35
    reference_images = [Image.open(rip) for rip in reference_images_path]
    reference_images = [image.convert("RGB") for image in reference_images]
    run_ref = Image.open('images/run_symbol.png')
    run_ref = run_ref.convert("RGB")
    rock_used = False
    out_of_park = True
    not_done = True

    while not_done:
        rand_delta = random.randint(0,3) + random.random()

        run_screen = pyautogui.screenshot(region=(539, 740, 145, 36))
        run_diff = calculate_difference(run_screen, run_ref)
        ref_images = [(ri, pyautogui.screenshot(region=ref_images_coords[rck])) for ri, rck in zip(reference_images, ref_images_keys)]
        diffs = [calculate_difference(ri[0], ri[1]) for ri in ref_images]
        min_diff = min(diffs)
        min_idx = diffs.index(min(diffs))
    
        if min_idx == 0 or min_idx == 1:
            if diffs[min_idx] <= max_diff:
                if rock_used:
                    # print(0)
                    move_mouse_to_point(pointer_coordinates['ball'][0], pointer_coordinates['ball'][1])
                    pyautogui.click()
                    rock_used = False
                    time.sleep(14.1 + rand_delta)
                    move_mouse_to_point(pointer_coordinates['close_window'][0], pointer_coordinates['close_window'][1])
                    pyautogui.click()
                    rand_delta = random.randint(0,3) + random.random()
                    time.sleep(1.1 + rand_delta)
                else:
                    # print(1)
                    move_mouse_to_point(pointer_coordinates['rock'][0], pointer_coordinates['rock'][1])
                    pyautogui.click()
                    rock_used = True
                    time.sleep(4.1 + rand_delta)
            else:
                if run_diff < 3:
                    # print(2)
                    move_mouse_to_point(pointer_coordinates['run'][0], pointer_coordinates['run'][1])
                    pyautogui.click()
                    rock_used = False
                    time.sleep(2.1 + rand_delta)
                else:
                    # print(3)
                    move_mouse_to_point(pointer_coordinates['rod'][0], pointer_coordinates['rod'][1])
                    pyautogui.click()
                    rock_used = False
                    time.sleep(4.1 + rand_delta)

        elif min_idx == 2:
            if diffs[min_idx] <= max_diff:
                # print(4)
                move_mouse_to_point(pointer_coordinates['baloon'][0], pointer_coordinates['baloon'][1])
                pyautogui.click()
                rock_used = False
                time.sleep(1 + rand_delta)
            else:
                if run_diff < 3:
                    # print(5)
                    move_mouse_to_point(pointer_coordinates['run'][0], pointer_coordinates['run'][1])
                    pyautogui.click()
                    rock_used = False
                    time.sleep(2.1 + rand_delta)
                else:
                    # print(6)
                    move_mouse_to_point(pointer_coordinates['rod'][0], pointer_coordinates['rod'][1])
                    pyautogui.click()
                    rock_used = False
                    time.sleep(4.1 + rand_delta)

        elif min_idx == 3:
            if diffs[min_idx] <= max_diff:
                # print(7)
                move_mouse_to_point(pointer_coordinates['baloon'][0], pointer_coordinates['baloon'][1])
                pyautogui.click()
                rock_used = False
                time.sleep(6 + rand_delta)
            else:
                if run_diff < 3:
                    # print(8)
                    move_mouse_to_point(pointer_coordinates['run'][0], pointer_coordinates['run'][1])
                    pyautogui.click()
                    rock_used = False
                    time.sleep(3.1 + rand_delta)
                else:
                    # print(9)
                    move_mouse_to_point(pointer_coordinates['rod'][0], pointer_coordinates['rod'][1])
                    pyautogui.click()
                    rock_used = False
                    time.sleep(4.1 + rand_delta)

        elif min_idx == 4:
            if diffs[min_idx] <= max_diff:
                # print(10)
                move_mouse_to_point(pointer_coordinates['baloon'][0], pointer_coordinates['baloon'][1])
                pyautogui.click()
                rock_used = False
                time.sleep(0.5 + rand_delta)
                pyautogui.click()
                time.sleep(0.5 + rand_delta)
                pyautogui.click()
                time.sleep(0.5 + rand_delta)
                pyautogui.click()
                time.sleep(0.5 + rand_delta)
                not_done = False
            else:
                if run_diff < 3:
                    # print(8)
                    move_mouse_to_point(pointer_coordinates['run'][0], pointer_coordinates['run'][1])
                    pyautogui.click()
                    rock_used = False
                    time.sleep(3.1 + rand_delta)
                else:
                    # print(9)
                    move_mouse_to_point(pointer_coordinates['rod'][0], pointer_coordinates['rod'][1])
                    pyautogui.click()
                    rock_used = False
                    time.sleep(4.1 + rand_delta)


if __name__ == "__main__":
    main()
