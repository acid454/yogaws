function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function do_show_element(e, list, idx, _thumbnails_path) {
    let node = document.createElement('li');
    let header = document.createElement('h3');
    let elem_content_div = document.createElement('div');
    
    header.textContent = e.caption;
    header.className = "wourkout_list_h3";
    elem_content_div.className = "element_content_left";
    if (e.properties != null) {
        var prop_table = document.createElement('table');

        
        /* prop_table.style.border = "1px solid #000" */
        prop_table.style.width = "100%"
        for (const [prop_idx, prop_descr] of Object.entries(e.properties)) {
            let tbl_r = document.createElement('tr');
            let tbl_d = document.createElement('td');

            /* tbl_d.style.border = "1px solid #000" */
            
            tbl_d.textContent = prop_descr.caption + "\xa0\xa0";
            tbl_r.appendChild(tbl_d);
            tbl_d = document.createElement('td');

            let num_div = document.createElement('div');
            num_div.className = "number";

            let btn_minus = document.createElement('button');
            btn_minus.className = "number-minus";
            btn_minus.type = "button";
            btn_minus.addEventListener("click", function (ev) { this.nextElementSibling.stepDown(); this.nextElementSibling.dispatchEvent(new Event('change')); } )
            btn_minus.textContent = "-";

            let btn_plus = document.createElement('button');
            btn_plus.className = "number-plus";
            btn_plus.type = "button";
            btn_plus.addEventListener("click", function (ev) { this.previousElementSibling.stepUp(); this.previousElementSibling.dispatchEvent(new Event('change')); } )
            btn_plus.textContent = "+";
            
            let inp = document.createElement('input');
            inp.type = "number";
            inp.value = prop_descr.value;
            inp.id = prop_descr.id;
            inp.className = "prop_input";
            inp.addEventListener("change", function (ev) {
                let params = {
                    "property_id": ev.target.id,
                    "value": event.target.value
                }

                let xhr = new XMLHttpRequest; 
                xhr.open("POST", "/modify_workout_params", true); 
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken')); 
                xhr.setRequestHeader('Content-type', 'application/json; charset=UTF-8')
                xhr.send(JSON.stringify(params)) // Make sure to stringify
                //xhr.onload = function() {
                //    console.log(`xhr status code: ${xhr.status}`)
                //}
            });

            num_div.appendChild( btn_minus );
            num_div.appendChild( inp );
            num_div.appendChild( btn_plus );
            tbl_d.appendChild( num_div );
            tbl_r.appendChild(tbl_d);
            prop_table.appendChild(tbl_r);
        }
    }
    elem_content_div.appendChild(prop_table)


    elem_preview_div = document.createElement('div');
    elem_preview_div.className = "element_content_right";
    img_preview = document.createElement('img');
    img_preview.src = _thumbnails_path + e.preview_img + '.png'
    elem_preview_div.appendChild(img_preview)
    /* console.log(e.preview_img) */


    let elem_div = document.createElement('div');
    elem_div.appendChild(elem_content_div)
    elem_div.appendChild(elem_preview_div)

    node.appendChild(header);
    node.appendChild(elem_div);
    node.id = "asana_element_" + idx;
    node.style = "--i: " + idx;
    list.appendChild(node);
}

function select_workout(_id, _thumbnails_path) {
    document.getElementById('main_centered_display').style.display='none';
    let xhr = new XMLHttpRequest();
    xhr.open('GET', '/view_workout?no_sounds=true&id=' + _id, false);
    xhr.send();
    if (xhr.status != 200) {
        console.log("Fail to load workout " + _id + " with status " + xhr.status);
        return;
    }
    
    const workout = JSON.parse(xhr.responseText)
    document.getElementById('caption').textContent = workout.caption;

    let list = document.getElementById('asanas_list');
    let idx = 0;
    
    list.innerHTML = '';
    /* console.log(workout) */
    for (i = 0; i < workout.sets.length; i++) {
        if (workout.sets[i].visible)
            do_show_element(workout.sets[i], list, idx++, _thumbnails_path)
        else {
            for (j = 0; j < workout.sets[i].asanas.length; j++)
                do_show_element(workout.sets[i].asanas[j], list, idx++, _thumbnails_path)
        }
    }
    
    list.style = "--length: " + idx;
    document.getElementById('runit_href').setAttribute('onclick','save_workout_local_storage("' + workout.id + '");');
    document.getElementById('total_time_value').textContent = workout.total_time; 
    document.getElementById('main_workout_list_display').style.display = '';
}

function setup_collapsible_list_height() {
    var coll = document.getElementsByClassName("collapsible");
    var i;

    for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
            this.classList.toggle("collapsible_content_active");
            var content = this.nextElementSibling;
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    }
}