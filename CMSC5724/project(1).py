




def useMarginPerceptron(R_val):
    stop_flag = False
    iteration_num = 0
    w = 0
    R = R_val
    r_guess = 0
    while not stop_flag:
        iteration_num = 1
        r_guess = R/(2**(iteration_num-1))
        iteration_limit = 12*(R**2)/((r_guess/2)**2)
        while True:
            stop_flag,w = marginPerceptron(r_guess)
            iteration_num += 1
            if iteration_num > iteration_limit:
                break

    print("The Margin Perceptron ends at "+iteration_num+": The current r_guess is "+r_guess+" and current w is "+w)



