# TextExtractor_Pratilipi
Simply extracts texts from an image using the PIL library of python and shows on the web app.

<h3>Installation </h3>

1. **clone the repository.**

   ```shell
   $git clone https://github.com/MuskanPaliwal/TextExtractor_Pratilipi.git

   ```
2. **navigate to downloaded folder.**

   ```shell
   $cd TextExtractor_Pratilipi

   ```
3. **set up virtual environment.**

   ```shell
   #windows
   
   $py -3 -m venv venv
   
   #linux/mac OS
   
   $python3 -m venv venv

   ```
4. **activate virtual environment.**

   ```shell
   #windows

   $venv\Scripts\activate
   
   #linux/mac OS
   
   $source venv/bin/activate

   ```
5. **install flask & other required dependencies**
    ```shell
    
    #windows
    

   $pip install -r requirements.txt
   
   #linux/mac OS
   
  
   $pip3 install -r requirements.txt

   ```
  
6. **Tesseract installation - for Windows OS**
    ```shell
  
    $ sudo apt install tesseract-ocr
  
    ```

7. **setup flask environment and run app**
    ```shell

    #windows
    
   $set FLASK_APP=app.py
   $set FLASK_ENV=development
   $flask run

   #linux/mac OS

   $export FLASK_APP=app.py
   $export FLASK_ENV=development
   $flask run
