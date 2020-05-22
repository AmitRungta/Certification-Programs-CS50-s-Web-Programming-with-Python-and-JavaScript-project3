function validateStatusUpdateForm( orderid)
{
    let formnodename = `update_status-${orderid}` ;
    let formnode = document.forms[formnodename] ;
    let newstatus = formnode["status"].value ;
    let originalstatus = formnode["original-status"].value ;
    if ( newstatus === originalstatus )
        return false ; // no need to change the status...
    confirmationstring = `Are you sure that you want to mark the order as '${newstatus}'?`;
    return confirm(confirmationstring) ;
}

