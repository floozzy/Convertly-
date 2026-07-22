import cv2



def detect_faces(path):

    try:

        image = cv2.imread(
            path
        )


        if image is None:

            return None



        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )



        cascade = cv2.CascadeClassifier(

            cv2.data.haarcascades
            +
            "haarcascade_frontalface_default.xml"

        )



        faces = cascade.detectMultiScale(

            gray,

            scaleFactor=1.1,

            minNeighbors=5

        )



        result = {


            "count":

                len(faces),


            "faces":

                []

        }



        height, width = gray.shape



        for x, y, w, h in faces:


            result["faces"].append(

                {

                    "x":

                        int(x),


                    "y":

                        int(y),


                    "width":

                        int(w),


                    "height":

                        int(h),



                    "position":

                        {

                            "x_percent":

                                round(
                                    x / width * 100,
                                    1
                                ),


                            "y_percent":

                                round(
                                    y / height * 100,
                                    1
                                )

                        }

                }

            )



        return result



    except Exception:

        return None
