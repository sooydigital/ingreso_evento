
var DOM_IDS = {
    FORM_ID_CODE: 'id_code',
    FORM_INPUT_TOKEN: 'csrfmiddlewaretoken',
    BTN_SENT: 'btn_sent',
    ID_MESSAGE: 'message',
    ID_FORM: 'formulario'
}

$('#'+DOM_IDS.BTN_SENT).on("click", validarPeople)

function validarPeople() {
    code = $('#' + DOM_IDS.FORM_ID_CODE).val()
    token = $(`[name='${DOM_IDS.FORM_INPUT_TOKEN}']`).val()
    data={
        "code": code,
        "csrfmiddlewaretoken": token,
    }
    updateRegistro(data, updateRegistroSuccessCallback, updateRegistroErrorCallback)

}

function hidenform(){
    $('#'+DOM_IDS.ID_FORM).addClass('hidden')
}

function  updateRegistroSuccessCallback (data)  {
    console.log('data', data)
    console.log('show mensajes')
    hidenform()
    mensaje = data['message']
    $('#' + DOM_IDS.ID_MESSAGE).html(
        mensaje
    )

}

function  updateRegistroErrorCallback() {
    console.log('salio un error ')

}

var updateRegistro = (data, successCallback, errorCallback) => {
      var url = `/api/validate`
      $.ajax({
            type: 'POST',
            url,
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            contentType: 'application/json; charset=utf-8',

            dataType : 'json',
            data: JSON.stringify(data),
            error: errorCallback,
            success: successCallback
      });
};


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}