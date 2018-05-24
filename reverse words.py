def reverseWords(input):
  a = input.split(" ")
  a=a[-1::-1]
  output = ' '.join(a)
  return output
if __name__ == "__main__":
    input = 'kavi sharmi'
    print reverseWords(input)
                                 
