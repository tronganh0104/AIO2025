import random
import math

def cal_activation_function():
    num_samples = input("Input number of samples (integer number) which are generated: ")
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return
    num_samples = int(num_samples)
    loss_name = input("Input loss name: ")
    final_loss = 0.0
    for n in range(num_samples):
        predict = random.uniform(0, 10)
        predict = round(predict, 2)
        target = random.uniform(0, 10)
        target = round(target, 2)
        current_loss = 0
        if loss_name == "MAE":
            current_loss = abs(predict - target)
        elif loss_name == "MSE" or loss_name == "RMSE":
            current_loss = (predict - target)**2
        current_loss = round(current_loss, 2)
        final_loss += current_loss
        print(f"loss_name: {loss_name}, sample: {n}: pred: {predict} target: {target} loss: {current_loss}")
    final_loss = final_loss/num_samples
    if loss_name == "RMSE":
        final_loss = math.sqrt(final_loss)
    print(f"final {loss_name}: {final_loss}")

cal_activation_function()