from enum import Enum

# Set bands
class Bands(Enum):
    RGB = "RGB"
    INFRARED = "infrared"
    ALL = "all"

# Set remote file paths and directories for ben-ge (small)
class RemoteFilesAndDirectoryReferencesSmall():
    # Files
    ESA_WORLD_COVER_CSV_TRAIN = "/ds2/remote_sensing/ben-ge/ben-ge-s/data-index/ben-ge-s-train.csv"
    ESA_WORLD_COVER_CSV_VALIDATION = "/ds2/remote_sensing/ben-ge/ben-ge-s/data-index/ben-ge-s-validation.csv"
    ESA_WORLD_COVER_CSV_TEST = "/ds2/remote_sensing/ben-ge/ben-ge-s/data-index/ben-ge-s-test.csv"
    SENTINEL_1_2_METADATA_CSV = "/ds2/remote_sensing/ben-ge/ben-ge-s/ben-ge-s_sentinel12_meta.csv"

    # Directories
    SENTINEL_1_DIRECTORY = "/ds2/remote_sensing/ben-ge/ben-ge-s/sentinel-1/s1_npy/"
    SENTINEL_2_DIRECTORY = "/ds2/remote_sensing/ben-ge/ben-ge-s/sentinel-2/s2_npy/"
    ESA_WORLD_COVER_DIRECTORY = "/ds2/remote_sensing/ben-ge/ben-ge-s/esaworldcover/"
    ERA5_CSV = "/ds2/remote_sensing/ben-ge/ben-ge-s/ben-ge-s_era-5.csv"

# Set remote file paths and directories for ben-ge (small)
class RemoteFilesAndDirectoryReferencesLarge():
    # Files
    ESA_WORLD_COVER_CSV_TRAIN = "/ds2/remote_sensing/ben-ge/ben-ge/data-index/ben-ge-train.csv"
    ESA_WORLD_COVER_CSV_VALIDATION = "/ds2/remote_sensing/ben-ge/ben-ge/data-index/ben-ge-validation.csv"
    ESA_WORLD_COVER_CSV_TEST = "/ds2/remote_sensing/ben-ge/ben-ge/data-index/ben-ge-test.csv"
    SENTINEL_1_2_METADATA_CSV = "/ds2/remote_sensing/ben-ge/ben-ge/ben-ge_meta.csv"

    # Directories
    SENTINEL_1_DIRECTORY = "/ds2/remote_sensing/ben-ge/ben-ge/sentinel-1/"
    SENTINEL_2_DIRECTORY = "/ds2/remote_sensing/ben-ge/ben-ge/sentinel-2/"
    ESA_WORLD_COVER_DIRECTORY = "/ds2/remote_sensing/ben-ge/ben-ge/esaworldcover/npy/"
    ERA5_CSV = "/ds2/remote_sensing/ben-ge/ben-ge/era-5/ben-ge_era-5.csv"

# Set local file paths and directories (large)
class LocalFilesAndDirectoryReferences():
    ESA_WORLD_COVER_CSV_TRAIN = "/Users/nicolaskesseli/Desktop/Uni/master-thesis.nosync/data/ben-ge-s/data-index/ben-ge-s-train.csv"
    ESA_WORLD_COVER_CSV_VALIDATION = "/Users/nicolaskesseli/Desktop/Uni/master-thesis.nosync/data/ben-ge-s/data-index/ben-ge-s-validation.csv"
    ESA_WORLD_COVER_CSV_TEST = "/Users/nicolaskesseli/Desktop/Uni/master-thesis.nosync/data/ben-ge-s/data-index/ben-ge-s-test.csv"

    SENTINEL_1_2_METADATA_CSV = "/Users/nicolaskesseli/Desktop/Uni/master-thesis.nosync/data/ben-ge-s/ben-ge-s_sentinel12_meta.csv"
    SENTINEL_1_DIRECTORY = "/Users/nicolaskesseli/Desktop/Uni/master-thesis.nosync/data/ben-ge-s/sentinel-1/s1_npy/"
    SENTINEL_2_DIRECTORY = "/Users/nicolaskesseli/Desktop/Uni/master-thesis.nosync/data/ben-ge-s/sentinel-2/s2_npy/"
    ESA_WORLD_COVER_DIRECTORY = "/Users/nicolaskesseli/Desktop/Uni/master-thesis.nosync/data/ben-ge-s/esaworldcover/"
    ERA5_CSV = "/Users/nicolaskesseli/Desktop/Uni/master-thesis.nosync/data/ben-ge-s/ben-ge-s_era-5.csv"
    GLO_30_DIRECTORY = '/Users/nicolaskesseli/Desktop/Uni/master-thesis.nosync/data/ben-ge-s/glo-30_dem'

# Images
S1_IMG_KEY = "s1_img"
S2_IMG_KEY = "s2_img"
WORLD_COVER_IMG_KEY = "world_cover_img"
ALTITUDE_IMG_KEY = "altitude_img"
STACKED_IMAGE_KEY = "stacked_img"
# Labels
MULTICLASS_LABEL_KEY = "multiclass_label"
# File data type
NUMPY_DTYPE = "float32"