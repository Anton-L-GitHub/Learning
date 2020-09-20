def something_went_wrong():
    try:
        raise Exception("something went wrong")
    except Exception as e:
        print(e)


something_went_wrong()
