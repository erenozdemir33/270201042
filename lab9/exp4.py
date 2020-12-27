def sleep(time) :
  if time == 0 :
    print("Time is finished!!!")
    return
  else :
    print("waits for", time ,"seconds")
    return sleep(time - 1)

sleep(5)