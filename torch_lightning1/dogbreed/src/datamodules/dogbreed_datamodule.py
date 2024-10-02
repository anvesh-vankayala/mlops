import os
import lightning as pl
from pathlib import Path
from typing import Union,Tuple
from torchvision.datasets.utils import download_and_extract_archive

class DogBreedDataModule(pl.LightningDataModule):
    def __init__(self,
                data_dir: Union[str, Path] = "data",
                num_worker: int = 0,
                batch_size:int = 8,
                splits: Tuple[float,float,float] = (0.8,0.1,0.1),
                pin_memory : bool = False
                ):
        
        super.__init__()
        self._data_dir = Path(data_dir)
        self._num_worker = num_worker
        self._batch_size = batch_size
        self._splits = splits
        self._pin_memory = pin_memory
        self._dataset = None

    def prepare_data(self) -> None:
        "This method downloads the images if not already downloaded and extracted"
        dataset_path = self._data_dir/'dog_breed_filtered'
        if not dataset_path.exists():
            download_and_extract_archive(
                url= '',
                download_root = self._data_dir,
                remove_finished = True
                                        )
        return super().prepare_data()



        
