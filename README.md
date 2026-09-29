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
Once you are in the directory, give ./requirements file permission to run. 

```bash
chmod +x requirements.sh
```
Then run the requirments. 

```bash
./requirements.sh
```

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