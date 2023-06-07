from make_dataset import make_data
from train_model import training_montage
from predict_sub import predict_subreddit



make_data() #asks to overwrite or create a new csv file with reddit data
training_montage() #takes saved csv, converts back to df, trains model, saves model instance as a pickle
    

u_input = input("Please input a title for recommendation:")

while u_input != "quit":

    
    answer = predict_subreddit(u_input)
    print(answer)
    u_input = input("Please input a title for recommendation:")