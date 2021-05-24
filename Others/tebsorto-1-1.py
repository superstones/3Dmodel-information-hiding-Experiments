import torch
def data_normal_2d(orign_data,dim="col"):
	"""
	针对于2维tensor归一化
	可指定维度进行归一化，默认为行归一化
	参数1为原始tensor，参数2为默认指定行，输入其他任意则为列
    """
    if dim == "col":
        dim = 1
        d_min = torch.min(orign_data,dim=dim)[0]
        for idx,j in enumerate(d_min):
            if j < 0:
                orign_data[idx,:] += torch.abs(d_min[idx])
                d_min = torch.min(orign_data,dim=dim)[0]
    else:
        dim = 0
        d_min = torch.min(orign_data,dim=dim)[0]
        for idx,j in enumerate(d_min):
            if j < 0:
                orign_data[idx,:] += torch.abs(d_min[idx])
                d_min = torch.min(orign_data,dim=dim)[0]
    d_max = torch.max(orign_data,dim=dim)[0]
    dst = d_max - d_min
    if d_min.shape[0] == orign_data.shape[0]:
        d_min = d_min.unsqueeze(1)
        dst = dst.unsqueeze(1)
    else:
        d_min = d_min.unsqueeze(0)
        dst = dst.unsqueeze(0)
    norm_data = torch.sub(orign_data,d_min).true_divide(dst)
    return norm_data

x = torch.randint(low=-10,high=10,size=(3,6))
data_normal_2d(x)
tensor([[1.0000, 0.8182, 0.4545, 0.0000, 0.8182, 0.2727],
        [0.6154, 0.5385, 0.5385, 0.0769, 0.0000, 1.0000],
        [0.4444, 0.3889, 0.0000, 0.2778, 1.0000, 0.5000]])
