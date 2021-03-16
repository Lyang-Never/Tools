## COCO detection
```
from torchvision.dataset import CocoDetection

# 源码如下：
class CocoDetection(VisionDataset):
    """`MS Coco Detection <https://cocodataset.org/#detection-2016>`_ Dataset.

    Args:
        root (string): Root directory where images are downloaded to.
        annFile (string): Path to json annotation file.
        transform (callable, optional): A function/transform that  takes in an PIL image
            and returns a transformed version. E.g, ``transforms.ToTensor``
        target_transform (callable, optional): A function/transform that takes in the
            target and transforms it.
        transforms (callable, optional): A function/transform that takes input sample and its target as entry
            and returns a transformed version.
    """

    def __init__(
        self,
        root: str,
        annFile: str,
        transform: Optional[Callable] = None,
        target_transform: Optional[Callable] = None,
        transforms: Optional[Callable] = None,
    ):
        super().__init__(root, transforms, transform, target_transform)
        from pycocotools.coco import COCO

        self.coco = COCO(annFile)
        self.ids = list(sorted(self.coco.imgs.keys()))

    def _load_image(self, id: int) -> Image.Image:
        path = self.coco.loadImgs(id)[0]["file_name"]
        return Image.open(os.path.join(self.root, path)).convert("RGB")

    def _load_target(self, id) -> List[Any]:
        return self.coco.loadAnns(self.coco.getAnnIds(id))

    def __getitem__(self, index: int) -> Tuple[Any, Any]:
        id = self.ids[index]
        image = self._load_image(id)
        target = self._load_target(id)

        if self.transforms is not None:
            image, target = self.transforms(image, target)

        return image, target

    def __len__(self) -> int:
        return len(self.ids)


```

```
可以直接继承上述CocoDetection
注意，__init__中super().__init__(img_paths,anno_path)
__getitem__中 img,anno = super().__getitem__(index)

百变不离其宗：
from pycocotools.coco import COCO
self.coco = COCO(anFile)
self.ids = list(sorted(self.coco.img.keys()))

# 由id获取imgpath,id是int类型，来自于self.ids
path = self.coco.loadImgs(id)[0]['file_name']

# 由id获取anno,anno是一个list，
anno = self.coco.loadAnns(self.coco.getAnnsIds(id))
ann = [o for o in anno if o['iscrowd'] == 0]
boxes = [o['bbox'] for o in anno]  # xywh

# 类别
self.coco.getCatIds() 是所有类别的list（里面是数字，代表不同类别）
category2id = [k:i+1 for i,k in enumerate(self.coco.getCatIds())]
id2category = [v:k for k,v in category2id.items()]

# mean,std
self.mean=[0.40789654, 0.44719302, 0.47026115]
self.std=[0.28863828, 0.27408164, 0.27809835]


```

## COCO VOC数据格式
![image](https://user-images.githubusercontent.com/56187355/111309286-aec08100-8696-11eb-9e42-b647674b595b.png)
![image](https://user-images.githubusercontent.com/56187355/111309316-b97b1600-8696-11eb-94c1-97422c9fef23.png)
