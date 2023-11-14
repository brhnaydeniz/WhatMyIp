import socket;
check = input(
  "IP adresinizi öğrenmek istiyor musunuz? (y/n):"); 
if check == 'n':    
   exit(); 
else:    
  print("\nIP adresiniz: ",end="");   
  print(socket.gethostbyname(socket.gethostname()));