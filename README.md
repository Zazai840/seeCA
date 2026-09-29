# SeeCA
The purpose of this project is to produce simple, one dimensional Cellular Automata in your terminal.

## Installation 
```bash
git clone https://github.com/Zazai840/seeCA
```
Then move into the root directory of the project. 
```bash
cd seeCA
```
Once you are in the directory, install requirements. 

```bash
python3 -m pip install -r requirements.txt
```
You may need to start a [virtual environment][https://docs.python.org/3/library/venv.html#creating-virtual-environments] before you install this projects requirements. 

## Usage 
In the virtual environment, run in terminal:
```bash
python3 main.py [rule] [timesteps] 
```
Rule is a number between 0 and 256.
Timesteps are the amount of timesteps that should pass to form the image. A good start is 100 time steps. 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)