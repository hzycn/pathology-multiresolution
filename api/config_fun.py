import os
# sys.path.append('../')
import ConfigParser

class config():
    def __init__(self, cfg_file = 'config/path.cfg'):

        cfg = ConfigParser.SafeConfigParser()
        cfg.read(cfg_file)
        # read content
        ## default
        ### folder
        self.normal_data_folder = cfg.get('DEFAULT', 'normal_data_folder')
        self.tumor_data_folder = cfg.get('DEFAULT', 'tumor_data_folder')
        self.tumor_anno_folder = cfg.get('DEFAULT', 'tumor_anno_folder')
        self.result_folder = cfg.get('DEFAULT', 'result_folder')
        self.target_level = cfg.getint('DEFAULT', 'target_level')
        ### others
        self.img_ext = cfg.get('DEFAULT', 'img_ext')
        ## PREPROCESS
        ### folder
        self.cache_folder = cfg.get('PREPROCESS', 'cache_folder')
        self.split_folder = cfg.get('PREPROCESS', 'split_folder')
        self.vis_ov_mask_folder = cfg.get('PREPROCESS', 'vis_ov_mask_folder')
        self.vis_patch_folder = cfg.get('PREPROCESS', 'vis_patch_folder')
        self.vis_pos_patch_folder = cfg.get('PREPROCESS', 'vis_pos_patch_folder')
        self.vis_neg_patch_folder = cfg.get('PREPROCESS', 'vis_neg_patch_folder')
        self.patch_save_folder = cfg.get('PREPROCESS', 'patch_save_folder')
        self.vis_hdf5_folder = cfg.get('PREPROCESS', 'vis_hdf5_folder')

        ### number
        self.val_normal = cfg.getint('PREPROCESS', 'val_normal')
        self.val_tumor = cfg.getint('PREPROCESS', 'val_tumor')
        self.patch_size = cfg.getint('PREPROCESS', 'patch_size')
        self.pos_patch_num_in_file = cfg.getint('PREPROCESS', 'pos_patch_num_in_file')
        self.neg_patch_num_in_file = cfg.getint('PREPROCESS', 'neg_patch_num_in_file')
        # self.patch_num_in_train = cfg.getint('PREPROCESS', 'patch_num_in_train')
        self.test_frac = cfg.getfloat('PREPROCESS', 'test_frac')
        self.alpha = cfg.getfloat('PREPROCESS', 'alpha')
        #self.max_frac = cfg.getfloat('PREPROCESS', 'max_frac')
        self.rescaled_times = cfg.getfloat('PREPROCESS', 'rescaled_times')
        self.vis_patch_prob = cfg.getfloat('PREPROCESS', 'vis_patch_prob')
        self.vis_hdf5_prob = cfg.getfloat('PREPROCESS', 'vis_hdf5_prob')

        ### files
        self.split_file = cfg.get('PREPROCESS', 'split_file')
        self.test_file = cfg.get('PREPROCESS', 'test_file')
        ### others
        self.redividing = cfg.getboolean('PREPROCESS', 'redividing')
        self.regenerate = cfg.getboolean('PREPROCESS', 'regenerate')
        self.vis_ov_mask = cfg.getboolean('PREPROCESS', 'vis_ov_mask')

        ## TRAIN
        ### folder
        self.train_folder = cfg.get('TRAIN', 'train_folder')
        self.patch_coor_folder = cfg.get('TRAIN', 'patch_coor_folder')
        self.patch_hdf5_folder = cfg.get('TRAIN', 'patch_hdf5_folder')
        self.checkpoint_folder = cfg.get('TRAIN', 'checkpoint_folder')
        ### file
        self.patch_hdf5_train_file_pre = cfg.get('TRAIN', 'patch_hdf5_train_file_pre')
        self.patch_hdf5_val_file_pre = cfg.get('TRAIN', 'patch_hdf5_val_file_pre')
        self.patch_coor_file = cfg.get('TRAIN', 'patch_coor_file')
        self.init_model_file = cfg.get('TRAIN', 'init_model_file')
        self.optim_state_file = cfg.get('TRAIN', 'optim_state_file')
        ### number
        self.patch_num_each_hdf5 = cfg.getint('TRAIN', 'patch_num_each_hdf5')
        self.model_info = cfg.getint('TRAIN', 'model_info')
        self.train_patch_frac = cfg.getfloat('TRAIN', 'train_patch_frac')
        self.val_patch_frac = cfg.getfloat('TRAIN', 'val_patch_frac')
        self.num_classes = cfg.getint('TRAIN', 'num_classes')
        self.num_neg_classes = cfg.getint('TRAIN', 'num_neg_classes')
        self.num_pos_classes = self.num_classes - self.num_neg_classes
        self.workers = cfg.getint('TRAIN', 'workers')
        self.batch_size = cfg.getint('TRAIN', 'batch_size')
        self.lr = cfg.getfloat('TRAIN', 'lr')
        self.momentum = cfg.getfloat('TRAIN', 'momentum')
        self.weight_decay = cfg.getfloat('TRAIN', 'weight_decay')
        self.max_epoch = cfg.getint('TRAIN', 'max_epoch')
        self.print_freq = cfg.getint('TRAIN', 'print_freq')
        self.train_slide_num_each_block = cfg.getint('TRAIN', 'train_slide_num_each_block')
        ### others
        self.model = cfg.get('TRAIN', 'model')
        self.model_pretrain = cfg.getboolean('TRAIN', 'model_pretrain')
        self.gpu_id = cfg.get('TRAIN', 'gpu_id')
        self.gpu_id = [int(id) for id in self.gpu_id.split(', ')]
        self.resume_training = cfg.getboolean('TRAIN', 'resume_training')
        self.train_file_wise = cfg.getboolean('TRAIN', 'train_file_wise')
        self.train_slide_wise = cfg.getboolean('TRAIN', 'train_slide_wise')

        # GENERATE MAP
        self.checkpoint_pth_file_level0 = cfg.get('GENERATE_MAP', 'checkpoint_pth_file_level0')
        self.optim_state_file_level0 = cfg.get('GENERATE_MAP', 'optim_state_file_level0')
        self.gm_foder = cfg.get('GENERATE_MAP', 'gm_foder')
        self.gm_stride = cfg.getint('GENERATE_MAP', 'gm_stride')
        self.windows_size = cfg.getint('GENERATE_MAP', 'windows_size')
        self.gm_batch_size = cfg.getint('GENERATE_MAP', 'gm_batch_size')
        self.gm_work_num = cfg.getint('GENERATE_MAP', 'gm_work_num')

        self.check_dirs()

    def check_dirs(self):
        self.check_dir(self.normal_data_folder)
        self.check_dir(self.tumor_data_folder)
        self.check_dir(self.tumor_anno_folder)
        self.check_dir(self.result_folder)
        self.check_dir(self.cache_folder)
        self.check_dir(self.split_folder)
        self.check_dir(self.vis_ov_mask_folder)
        self.check_dir(self.vis_patch_folder)
        self.check_dir(self.vis_pos_patch_folder)
        self.check_dir(self.vis_neg_patch_folder)
        self.check_dir(self.patch_save_folder)
        self.check_dir(self.patch_save_folder)
        # TRAIN
        self.check_dir(self.train_folder)
        self.check_dir(self.patch_coor_folder)
        self.check_dir(self.checkpoint_folder)
        self.check_dir(self.patch_hdf5_folder)
        self.check_dir(self.vis_hdf5_folder)
        # GENERATE MAP
        self.check_dir(self.gm_foder)

    def check_dir(self, dir):
        if not os.path.exists(dir):
            os.mkdir(dir)


if __name__ == '__main__':
    cfg = config()
    print(cfg)
