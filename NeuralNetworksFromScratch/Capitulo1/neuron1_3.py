inputs = [1, 2, 3, 4]
targets = [4, 6, 8, 10]

w = 0.1
b = 0.3
epochs = 300
learning_rate = 0.1

def predict(i):
  return w*i + b

#Train the network
for _ in range(epochs):
  pred = [predict(i) for i in inputs]
  errors = [(p - t)**2 for p, t in zip(pred, targets)] #Cost will generate overflow
  cost = sum(errors)/len(targets)
  ##############################################################################
  #Cost using the error derivetive
  errors_d = [2*(p - t) for p, t in zip(pred, targets)]
  weight_d = [e*i for e, i in zip(errors_d, inputs)]
  bias_d = [e*1 for e in errors_d]
  w-= learning_rate*sum(weight_d)/len(weight_d)
  b -= learning_rate*sum(bias_d)/len(bias_d)
  ##############################################################################
  #print(f"Targets: ", targets)
  #print(f"Predictions: ", pred)
  #print(f"Errors: ", errors)
  print(f"Weight: {w: .2f}, Bias: {b:.2f}, Cost: {cost:.2f}")

#Test the network:
test_inputs = [5, 6]
test_targets = [10, 12]
pred = [predict(i) for i in test_inputs]
for i, t, p in zip(test_inputs, test_targets, pred):
  print(f"input:{i}, target:{t}, pred:{p:.4f}")
