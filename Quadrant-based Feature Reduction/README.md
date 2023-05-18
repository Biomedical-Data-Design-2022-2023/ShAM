## Use Quadrant-based Feature Reduction
1. Generate quadrant masked images using files in the `masked_image_generation` or you can also use generated images in the `output_shap`.
   1. Gaussian-based: 
      1. Open `gaussian_masked_image_generator.py`.
      2. Change `filename` to your desired image directory.
      3. Run.
      4. It should produce images like bellow.

      ![img.png](readme_image/img1.png)
   2. Simple black-out:
       1. Open `masked_image_generator.py`.
       2. Change `filename` to your desired image directory.
       3. Run.
       4. It should produce images like bellow.
      
       ![img.png](readme_image/img.png)
   3. Inpainting-based:
       1. Run `gan_mask_generate.py`.
       2. It should generate masked file for inpainting.
       3. Follow the instruction in `Example Inpainting Code Guide.pdf` in the `Documentation` to generate cells one by one. 

       ![img.png](readme_image/img2.png)
   
2. Change the generated file directory in the python file under `shap_cal` to run shapley value calculation.
   1. Run the `shap` python file accordingly based on your generated images. i.e. if you use generate gaussian based images, run `shap_mike_withGaussianMask.py`.

## Demo
Can be found [here](https://github.com/Biomedical-Data-Design-2022-2023/ShAM/blob/main/Quadrant-based%20Feature%20Reduction/Quad_blackout_shapCal_pipeline.ipynb)

   
