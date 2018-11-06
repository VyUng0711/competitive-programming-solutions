def repeatedNumber(A):
      n = len(A)
      # real_sum = (n * (n + 1)) // 2
      # real_sum_squares = n * (n + 1) * (2 * n + 1) / 6
      real_sum = 0
      real_sum_squares = 0
      A_sum = 0
      A_sum_squares = 0
      for i in range(1, n + 1):
          real_sum += i
          real_sum_squares += i ** 2
      for j in range(0, n):
          A_sum += A[j]
          A_sum_squares += A[j] ** 2 

            
      x = real_sum - A_sum
      y = real_sum_squares - A_sum_squares
      
      
      x = B - A
      y = (B - A)(B + A)
      y/x = B + A
      x = B - A
      
      B = (x + y/x) / 2
      
      A = B - x

      return [round(A), round(B)]
