#1.8 Zero Matrix

class ZeroMatrix():
    def display(self,row, col, matrix):
        for i in range(row):
            for j in range(col):
                print(matrix[i][j], end=" ")
            print()

    def matrix(self,row,col):
        matrix = []

        for i in range(row):
            a = []
            for j in range(col):
                a.append(int(input()))
            matrix.append(a)
        return matrix

    def matrix_edit(self,row,col,matrix):
        nullrow = []
        nullcol = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    nullrow.append(i)
                    nullcol.append(j)

        for i in range(row):
            for j in range(col):
                if i in nullrow or j in nullcol:
                    matrix[i][j] = 0

        return matrix


if __name__ == "__main__":
    row = 2
    col = 3
    obj = ZeroMatrix()
    matrix_create = obj.matrix(row,col)
    print("\n------------------------\n")
    obj.display(row,col,matrix_create)
    matrix_editing = obj.matrix_edit(row,col,matrix_create)
    print("\n------------------------\n")
    obj.display(row,col,matrix_editing)

#1.6 String compression
str1 = "aabcccccaaa"
count = 1
new_string =""
for i in range(len(str1)-1):
    if str1[i] == str1[i+1]:
        count +=1
    else:
        new_string += str1[i]+ str(count)
        count = 1
new_string += str1[1] +str(count)
print(new_string)

#1.5 OneAway
class Oneaway():
    def twostrings(self, str1, str2):
        len_str1 = len(str1)
        len_str2 = len(str2)
        count = abs(len_str1 - len_str2)
        result = True

        if count == 0:
            diff_count = 0
            for i in range(len_str1):
                if str1[i] != str2[i]:
                    diff_count += 1
                    if diff_count > 1:
                        result = False
                        break
        elif count == 1:
            if len_str1 > len_str2:
                result = self.check_one_delete(str1, str2)
            else:
                result = self.check_one_delete(str2, str1)
        else:
            result = False

        return result

    def check_one_delete(self, longer, shorter):
        i = 0
        j = 0
        diff_count = 0

        while i < len(longer) and j < len(shorter):
            if longer[i] != shorter[j]:
                diff_count += 1
                if diff_count > 1:
                    return False
                i += 1
            else:
                i += 1
                j += 1

        return True

if __name__ == '__main__':
    str1 = "pale"
    str2 = "pale"

    obj = Oneaway()
    res = obj.twostrings(str1, str2)
    print(res)

#1.4 Palindrome Permutation
class Permu_palindrome():
    def checkstring(self, str1):
        dict_str = dict()

        for chars in str1:
            if chars in dict_str:
                dict_str[chars] += 1
            else:
                dict_str[chars] = 1

        print(dict_str)

        odd_count = 0
        even_count = 0
        if len(str1) % 2 != 0:
            for i, j in dict_str.items():
                if dict_str[i] % 2 != 0:
                    odd_count += 1
        else:
            for i, j in dict_str.items():
                if dict_str[i] % 2 != 0:
                    even_count += 1

        if odd_count > 1 or even_count > 0:
            print("no permu - palindrome")
        else:
            print("permu - palindrome")

if __name__ == '__main__':
    str1 = 'obbo'
    obj_permu_palindrome = Permu_palindrome()
    obj_permu_palindrome.checkstring(str1)

