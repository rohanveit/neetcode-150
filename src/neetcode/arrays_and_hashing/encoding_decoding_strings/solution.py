class Solution:

    DELIMITER_LEN = 3

    def encode_strs(self, strings: list[str]) -> str:
        encoded_output = ""
        for string in strings:
            # add 3 digit number denoting how much chars the next string is
            encoded_output += self.format_number(len(string))
            encoded_output += string

        return encoded_output

    def decode_strs(self, encoded_str: str, delimiter_len: int = DELIMITER_LEN) -> str:
        pointer = 0
        output = list()
        #print(encoded_str)
        while pointer != len(encoded_str):
            next_str_len = int(encoded_str[pointer:pointer+delimiter_len])
            #print(next_str_len)
            pointer += delimiter_len
            next_str = encoded_str[pointer:pointer+next_str_len]
            #print(next_str)
            output.append(next_str)
            pointer += next_str_len
        return output




    def format_number(self, num: int, full_length: int = DELIMITER_LEN) -> str:
        num_digits = len(str(num))
        return ('0' * (full_length - num_digits)) + str(num)

if __name__ == "__main__":
    solution = Solution()
    # print(solution.encode_strs(['hello','world']))
    result = solution.decode_strs(solution.encode_strs(['hello', 'world']))
    print(result)
