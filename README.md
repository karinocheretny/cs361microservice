# cs361microservice

!------------------- required libraries ----------------------------------------------!<br />
 pip install trimesh<br />
 pip install numpy-stl meshio<br />
 pip install Flask<br />
!--------------------------------------------------------------------------------------!<br />


!---------------- helpful links and refrences -----------------------------------------!<br />
meshio documentation: https://github.com/nschloe/meshio<br />
numpy-stl documentation: https://numpy-stl.readthedocs.io/en/latest/<br />
trimesh documentation: https://trimsh.org/<br />
STL file format specification: https://en.wikipedia.org/wiki/STL_(file_format)<br />
OBJ file format specification: https://en.wikipedia.org/wiki/Wavefront_.obj_file<br />
!---------------------------------------------------------------------------------------!<br />


!------------------ request data -------------------------------------------------------!<br />
the microservice uses flask.request to request data. To request data, a user can upload <br />
a file using the flask app. that is being done with flask.request in converter_micro.py<br />
*click "upload" within the flask app<br />
!---------------------------------------------------------------------------------------!<br />


!--------------- recieve data-----------------------------------------------------------!<br />
the computer automatically downloads the converted file onto the users computer when they<br />
request data. that is being done in converter_micro.py with send_file(get_path, as_attachment=True)<br />
!---------------------------------------------------------------------------------------!<br />


!------------------- UML sequence diagram ----------------------------------------------!<br />
checkout uml.PNG<br />
!---------------------------------------------------------------------------------------!<br />
