import weyl_sequences_constants
import hilbert_series_constants
import utility


for n in range(2,8):
    hilbert_string = hilbert_series_constants.get_hilbert(n)
    current = utility.hilbert_string_to_list(hilbert_string)

    output = f'H_{n} = '

    while utility.get_first_coeff(current)[0] != 0:
        (first_coeff, first_power) = utility.get_first_coeff(current)


        weyl_num = utility.get_weyl_of_poly(current)

        negative = False

        if weyl_num < 0:
            current = [x * -1 for x in current]
            weyl_num = weyl_num * -1
            first_coeff = first_coeff * -1
            negative = True


        if weyl_num % first_coeff >= 2:
            break

        if weyl_num % first_coeff == 0:
            weyl_num = int(weyl_num / first_coeff)
        elif weyl_num % first_coeff == 1:
            weyl_num = int((weyl_num - 1) / first_coeff)

        weyl = weyl_sequences_constants.get_weyl(weyl_num)


        if weyl == None:
            break

        weyl = [x * first_coeff for x in weyl]

        scaled_weyl = utility.scale_polynomial(weyl, first_power)

        current = utility.sub_polynomials(current, scaled_weyl)

        negative_flag = ""
        if negative:
            negative_flag = "-"

        output = output + negative_flag + str(first_coeff) + " * A_" + str(weyl_num) + " X^" + str(first_power) + " + "
        

    output = output + " ..."
    print(output)

        
