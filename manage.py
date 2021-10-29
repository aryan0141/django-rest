def predictAction(height, dist, pipe_height, model_num):
    global currentPool
    # The height, dist and pipe_height must be between 0 to 1 (Scaled by SCREENHEIGHT)
    height = min(SCREENHEIGHT, height) / SCREENHEIGHT - 0.5
    dist = dist / 450 - 0.5  # Max pipe distance from player will be 450
    pipe_height = min(SCREENHEIGHT, pipe_height) / SCREENHEIGHT - 0.5
    neural_input = np.asarray([height, dist, pipe_height])
    neural_input = np.atleast_2d(neural_input)
    output_prob = currentPool[model_num].predict(neural_input, 1)[0]
    if output_prob[0] <= 0.5:
        # Perform the jump action
        return 1
    return 2


# Initialize all the models
currentPool = createModel(totalPlayers)
for idx in range(totalPlayers):
    fitness.append(-100)

Images = {}

