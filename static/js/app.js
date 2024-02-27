

function select_event(){
    const select = document.getElementById('selected-category')
    let selected = ''
    select.addEventListener('change', (e)=>{  
        e.preventDefault();
        
        if(select.value == 1){
            selected = 'Application';
        }
        else if(select.value == 2){
            selected = 'Security';
        }
        else if(select.value == 3) {
            selected = 'System';
        }
        else if(select.value == 4) {
            selected = 'Setup';
        }
        else if(select.value == 5) {
            selected = 'Active Directory';
        }
        else if(select.value == 6) {
            selected = 'DNS Server';
        }
    })
    return selected;
}
console.log(select_event())