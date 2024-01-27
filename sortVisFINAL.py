import pygame
import random
import math
import time

pygame.init()

 

class DrawInformation:

    BLACK = 0, 0, 0

    WHITE = 255, 255, 255

    GREEN = 0, 154, 0

    RED = 255, 0, 0

    BACKGROUND_COLOR = WHITE

 

    GRADIENTS = [

        (128, 128, 128),

        (160, 160, 160),

        (192, 192, 192)

    ]

 

    FONT = pygame.font.SysFont('bahnschrift', 20)

    LARGE_FONT = pygame.font.SysFont('bahnschrift', 35)

    SMALL_FONT = pygame.font.SysFont('bahnschrift', 15)

 

    SIDE_PAD = 100

    TOP_PAD = 150

 

    def __init__(self, width, height, lst):

        self.width = width

        self.height = height

 

        self.window = pygame.display.set_mode((width, height))

        pygame.display.set_caption("Sorting Algorithm Visualization")

        self.set_list(lst)

 

    def set_list(self, lst):

        self.lst = lst

        self.min_val = min(lst)

        self.max_val = max(lst)

 

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))

        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val)) - 1

        self.start_x = self.SIDE_PAD // 2

 

 

def draw(draw_info, algo_name, ascending, elapsed_time, time_complexity):

    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    if elapsed_time is not None:
        time_text = draw_info.SMALL_FONT.render(f"Time: {elapsed_time:.2f} seconds", 1, draw_info.BLACK)
        draw_info.window.blit(time_text, ((draw_info.width/2 - time_text.get_width()/2)-100, 130))
    
    if time_complexity:
        complexity_text = draw_info.SMALL_FONT.render(f"Time Complexity: {time_complexity}", 1, draw_info.BLACK)
        draw_info.window.blit(complexity_text, ((draw_info.width/2 - complexity_text.get_width()/2)+100, 130))


    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.GREEN)

    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2 , 5))

 

    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)

    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2 , 45))

 

    sorting = draw_info.FONT.render("I - Insertion Sort  |  B - Bubble Sort | S - Selection Sort", 1, draw_info.BLACK)

    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2 , 75))

 

    sorting = draw_info.FONT.render("M - Merge Sort  |  C - Count Sort   |  Q - Quick sort ", 1, draw_info.BLACK)

    draw_info.window.blit(sorting, ((draw_info.width/2 - sorting.get_width()/2)-5 , 105))

 
    #sorting_status = draw_info.SMALL_FONT.render(f"{'Sorting...' if sorting else 'Sorted!'}", 1, draw_info.BLACK)
    #draw_info.window.blit(sorting_status, (draw_info.width/2 - sorting_status.get_width()/2, 135))

    # Display elapsed time
    

    draw_list(draw_info)

    pygame.display.update()

 

 

def draw_list(draw_info, color_positions={}, clear_bg=False, update_display=True):

    lst = draw_info.lst
 

    if clear_bg:

        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD-5,

                        draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)

        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

 

    for i, val in enumerate(lst):

        x = draw_info.start_x + i * draw_info.block_width

        if val == draw_info.min_val:

            y = draw_info.height - (val - draw_info.min_val + 1) * draw_info.block_height

        else:

            y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

 

        color = draw_info.GRADIENTS[i % 3]

 

        if i in color_positions:

            color = color_positions[i]

 

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

        
        text = draw_info.SMALL_FONT.render(str(val), 1, draw_info.BLACK)
        text_rect = text.get_rect()
        text_rect.center = (x + draw_info.block_width // 2, y - 20)  # Adjust the position for text
        draw_info.window.blit(text, text_rect)

    if clear_bg:
        pygame.display.update()

    if update_display:
        pygame.display.update()

 

 

def generate_starting_list(n, min_val, max_val):

    lst = []

 

    for _ in range(n):

        val = random.randint(min_val, max_val)

        lst.append(val)

 

    #print(lst)

    return lst

 

 

def bubble_sort(draw_info, ascending=True):

    lst = draw_info.lst

 

    for i in range(len(lst) - 1):

        for j in range(len(lst) - 1 - i):

            num1 = lst[j]

            num2 = lst[j + 1]

 

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):

                lst[j], lst[j + 1] = lst[j + 1], lst[j]

                #draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True, update_display=False)
                yield True

    draw_list(draw_info, {}, True, update_display=True)
    return lst

 

def insertion_sort(draw_info, ascending=True):

    lst = draw_info.lst

 

    for i in range(1, len(lst)):

        current = lst[i]

 

        while True:

            ascending_sort = i > 0 and lst[i - 1] > current and ascending

            descending_sort = i > 0 and lst[i - 1] < current and not ascending

 

            if not ascending_sort and not descending_sort:

                break

 

            lst[i] = lst[i - 1]

            i = i - 1

            lst[i] = current

            #draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
            #draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True, update_display=False)
            draw_list(draw_info, {i-1: draw_info.GREEN, i: draw_info.RED}, True, update_display=False)


            yield True

 
    draw_list(draw_info, {}, True, update_display=True)
    return lst

 

def selection_sort(draw_info, ascending=True):

    lst = draw_info.lst

 

    for i in range(len(lst)):

        min_idx = i

        for j in range(i+1, len(lst)):

            if (lst[j] < lst[min_idx] and ascending) or (lst[j] > lst[min_idx] and not ascending):

                min_idx = j

 

        lst[i], lst[min_idx] = lst[min_idx], lst[i]

        #draw_list(draw_info, {i: draw_info.GREEN, min_idx: draw_info.RED}, True)
        #draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True, update_display=False)
        draw_list(draw_info, {i: draw_info.GREEN, min_idx: draw_info.RED}, True, update_display=False)


        yield True

 
    draw_list(draw_info, {}, True, update_display=True)
    return lst

 

def merge_sort(draw_info, ascending=True):

    lst = draw_info.lst

 

    def merge(arr, left, mid, right):

        temp = []

        i = left

        j = mid + 1

 

        while i <= mid and j <= right:

            if (arr[i] <= arr[j] and ascending) or (arr[i] >= arr[j] and not ascending):

                temp.append(arr[i])

                i += 1

            else:

                temp.append(arr[j])

                j += 1

 

        while i <= mid:

            temp.append(arr[i])

            i += 1

 

        while j <= right:

            temp.append(arr[j])

            j += 1

 

        for k in range(left, right + 1):

            arr[k] = temp[k - left]

            #draw_list(draw_info, {k: draw_info.GREEN}, True)
            #draw_list(draw_info, {k: draw_info.GREEN, j + 1: draw_info.RED}, True)
            #draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True, update_display=False)
            draw_list(draw_info, {k: draw_info.GREEN}, True, update_display=False)


            yield True

 

    def merge_sort_recursive(arr, left, right):

        if left < right:

            mid = (left + right) // 2

 

            yield from merge_sort_recursive(arr, left, mid)

            yield from merge_sort_recursive(arr, mid + 1, right)

 

            yield from merge(arr, left, mid, right)

 

    yield from merge_sort_recursive(lst, 0, len(lst) - 1)

    draw_list(draw_info, {}, True, update_display=True)
    return lst  

 

def count_sort(draw_info, ascending=True):

    lst = draw_info.lst

    min_val = draw_info.min_val

    max_val = draw_info.max_val

   

    value_range = max_val - min_val + 1

 

    count = [0] * value_range

 

    for num in lst:

        count[num - min_val] += 1

 

    sorted_lst = []

 

    if ascending:

        for i in range(value_range):

            while count[i] > 0:

                sorted_lst.append(i + min_val)

                count[i] -= 1

    else:

        for i in range(value_range - 1, -1, -1):

            while count[i] > 0:

                sorted_lst.append(i + min_val)

                count[i] -= 1

    for i in range(len(lst)):

        lst[i] = sorted_lst[i]

        #draw_list(draw_info, {i: draw_info.GREEN}, True)
        #draw_list(draw_info, {i: draw_info.GREEN, i + 1: draw_info.RED}, True)
        #draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True, update_display=False)
        draw_list(draw_info, {i: draw_info.GREEN}, True, update_display=False)


        yield True

    draw_list(draw_info, {}, True, update_display=True)
    return lst    

 

def quick_sort(draw_info, ascending=True):

    lst = draw_info.lst

 

    def partition(arr, low, high):

        pivot = arr[high]

        i = low - 1

 

        for j in range(low, high):

            if (arr[j] <= pivot and ascending) or (arr[j] >= pivot and not ascending):

                i += 1

                arr[i], arr[j] = arr[j], arr[i]

                draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True, update_display=False)

                yield True

 

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        #draw_list(draw_info, {i + 1: draw_info.GREEN, high: draw_info.RED}, True)
        #draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True, update_display=False)
        draw_list(draw_info, {i+1: draw_info.GREEN, high: draw_info.RED}, True, update_display=False)

        yield True

 

        return i + 1

 

    def quick_sort_recursive(arr, low, high):

        if low < high:

            pivot_index = yield from partition(arr, low, high)

 

            yield from quick_sort_recursive(arr, low, pivot_index - 1)

            yield from quick_sort_recursive(arr, pivot_index + 1, high)

    yield from quick_sort_recursive(lst, 0, len(lst) - 1)

    draw_list(draw_info, {}, True, update_display=True)
    return lst      

   

 

def main():

    run = True

    clock = pygame.time.Clock()

    time_complexities = {
    "Insertion Sort": "O(n^2)",
    "Bubble Sort": "O(n^2)",
    "Selection Sort": "O(n^2)",
    "Count Sort": "O(n+k)",
    "Merge Sort": "O(n log n)",
    "Quick Sort": "O(n^2) or O(n log n)",
    }

    n = 10

    min_val = 2

    max_val = 30

 

    lst = generate_starting_list(n, min_val, max_val)

    draw_info = DrawInformation(800, 700, lst)

    sorting = False

    ascending = True

 

    sorting_algorithm = bubble_sort

    sorting_algo_name = "Bubble Sort"

    sorting_algorithm_generator = None

    start_time =  None
    end_time = None
    elapsed_time = None
    time_complexity = None

    while run:
        clock.tick(5)

        if sorting:
            if start_time is None:
                start_time = time.time()
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
                end_time = time.time()
                elapsed_time = end_time - start_time
                time_complexity = time_complexities.get(sorting_algo_name, "")
                #print(f"Sorting completed in {elapsed_time:.2f} seconds")
                #print(f"Time Complexity: {time_complexity}")
                start_time = None
                end_time = None
        else:
            draw(draw_info, sorting_algo_name, ascending, elapsed_time, time_complexity)  # Pass time_complexity
            draw_list(draw_info, {}, True, update_display=True)
 

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

 

            if event.type != pygame.KEYDOWN:

                continue

 

            if event.key == pygame.K_r:

                lst = generate_starting_list(n, min_val, max_val)

                draw_info.set_list(lst)

                sorting = False

                elapsed_time = None
                time_complexity = None
                draw_list(draw_info, {}, True, update_display=True)

            elif event.key == pygame.K_SPACE and sorting == False:

                sorting = True

                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)

            elif event.key == pygame.K_a and not sorting:

                ascending = True

            elif event.key == pygame.K_d and not sorting:

                ascending = False

            elif event.key == pygame.K_i and not sorting:

                sorting_algorithm = insertion_sort

                sorting_algo_name = "Insertion Sort"

            elif event.key == pygame.K_b and not sorting:

                sorting_algorithm = bubble_sort

                sorting_algo_name = "Bubble Sort"

            elif event.key == pygame.K_s and not sorting:

                sorting_algorithm = selection_sort

                sorting_algo_name = "Selection Sort"

            elif event.key == pygame.K_c and not sorting:

                sorting_algorithm = count_sort

                sorting_algo_name = "Count Sort"            

            elif event.key == pygame.K_m and not sorting:

                sorting_algorithm = merge_sort

                sorting_algo_name = "Merge Sort"

            elif event.key == pygame.K_q and not sorting:

                sorting_algorithm = quick_sort

                sorting_algo_name = "Quick Sort"

    pygame.quit()

 

 

if __name__ == "__main__":

    main()