# cs361microservice

!------------------- required libraries ----------------------------------------------!
 pip install trimesh
 pip install numpy-stl meshio
 pip install Flask
!--------------------------------------------------------------------------------------!


!---------------- helpful links and refrences -----------------------------------------!
meshio documentation: https://github.com/nschloe/meshio
numpy-stl documentation: https://numpy-stl.readthedocs.io/en/latest/
trimesh documentation: https://trimsh.org/
STL file format specification: https://en.wikipedia.org/wiki/STL_(file_format)
OBJ file format specification: https://en.wikipedia.org/wiki/Wavefront_.obj_file
!---------------------------------------------------------------------------------------!


!------------------ request data -------------------------------------------------------!
the microservice uses flask.request to request data. To request data, a user can upload 
a file using the flask app. that is being done with flask.request in converter_micro.py
*click "upload" within the flask app
!---------------------------------------------------------------------------------------!


!--------------- recieve data-----------------------------------------------------------!
the computer automatically downloads the converted file onto the users computer when they
request data. that is being done in converter_micro.py with send_file(get_path, as_attachment=True)
!---------------------------------------------------------------------------------------!


!------------------- UML sequence diagram ----------------------------------------------!
checkout uml.PNG
!---------------------------------------------------------------------------------------!