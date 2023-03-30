from typing import List

# Skeleton code for even_List
def even_list(int_list: List[int]) -> List[int]:
    even_int_list = []
    for i in range(0, len(int_list)):
        if int_list[i] % 2 == 0:
            even_int_list.append(int_list[i])
    
    return even_int_list
    pass

# Skeleton code for even_List
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    pass

# Main function
def main():
    int_list = [1,2,3,4,5,6,7,8,9,10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_eve(even_int_list)
    print(output)

if __name__ == "__main__":
    main()
