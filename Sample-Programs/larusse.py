import sys

operand_a = int(sys.argv[1])
operand_b = int(sys.argv[2])
answer = 0

print("Multiplication of", operand_a, "and", operand_b, "is ", end="")
while operand_a !=1:
  if operand_a % 2 == 1:
    answer += operand_b
  operand_a //= 2
  operand_b *= 2

answer += operand_b
print(answer)
exit()


