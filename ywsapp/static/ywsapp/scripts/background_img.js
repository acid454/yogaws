function setup_background_image(res_path, main_bg_image) {
    background_img_id = sessionStorage.getItem('background_img_id');
    if (background_img_id == null) {
        background_img_id = main_bg_image;
        sessionStorage.setItem('background_img_id', background_img_id);
    }
    document.getElementById('main_centered_display').style.backgroundImage = "url('" + res_path + background_img_id + "')";
    document.getElementById('main_workout_list_display').style.display = 'none';
}
