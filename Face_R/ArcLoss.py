
```
class ArcLoss(SoftmaxCrossEntropyLoss):
    def __init__(self, classes, m=0.5, s=64, easy_margin=True, dtype="float32", **kwargs):
        super().__init__(**kwargs)
        assert s > 0.
        assert 0 <= m < (math.pi / 2)
        self.s = s
        self.m = m
        self.cos_m = math.cos(m)
        self.sin_m = math.sin(m)
        self.mm = math.sin(math.pi - m) * m
        self.threshold = math.cos(math.pi - m)
        self._classes = classes
        self.easy_margin = easy_margin
        self._dtype = dtype
        
    def hybrid_forward(self, F, pred, label, sample_weight=None, *args, **kwargs):
    
        ```
        # pred:(B,num_classes)
        # label:(B,) 其值的取值范围为（0，num_classes]
        ```
       
        
        ```
        # 这一部分，根据label挑选出来gt_pred,并将gt_pred中小于0的用zy_keep代替，这个操作通过F.where操作完成。
        # 这个cond/cond_v中的各个值来自于cos_t,cos_t中大于0的呢还是其本身，小于0的变为0，这样，在F.where中，
        # 若cond中的值大于0，则还为new_zy,否则为zy_keep.
        ```
        cos_t = F.pick(pred, label, axis=1)  # cos(theta_yi)  shape:(B,)
        if self.easy_margin:
            cond = F.Activation(data=cos_t, act_type='relu')
        else:
            cond_v = cos_t - self.threshold
            cond = F.Activation(data=cond_v, act_type='relu')

        new_zy = F.cos(F.arccos(cos_t) + self.m)  # cos(theta_yi + m)
        if self.easy_margin:
            zy_keep = cos_t
        else:
            zy_keep = cos_t - self.mm  # (cos(theta_yi) - sin(pi - m)*m)
        new_zy = F.where(cond, new_zy, zy_keep)
        
        ```
        # 这一部分，算出来new_zy 大于 cos_t的那部分，并将其加到原来pred对应的位置上。主要通过以下几个函数实现：
        # ① F.expand_dims()         在diff的第一维度上扩展一下（维度从0开始）
        # ② F.one_hot()             返回一个shape为（B,depth）one_hot,其中label中对应值所标识的位置为on_value,为表示的位置为off_value
        
        ```
        diff = new_zy - cos_t  # cos(theta_yi + m) - cos(theta_yi)
        diff = F.expand_dims(diff, 1)  # shape=(B, 1)
        gt_one_hot = F.one_hot(label, depth=self._classes, on_value=1.0, off_value=0.0, dtype=self._dtype)
        body = F.broadcast_mul(gt_one_hot, diff)
        pred = pred + body
        pred = pred * self.s

        return super().hybrid_forward(F, pred=pred, label=label, sample_weight=sample_weight)



```
