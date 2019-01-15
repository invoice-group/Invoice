
(function($, photo) {
	photo.getAllphoto=function(str){
		$.ajax({
    		type:"GET",
    		url:"http://trveller.d4smarter.com/image/getAll",
    		async:false,
    		dataType: 'json',
    		data:{
    			
    		},
    		success:function(res){
    			var j=res.data.list.length;
    			for(var i=0;i<j;i++){
    				str.val=str.val+"<li class='mui-table-view-cell mui-media mui-col-xs-6'><img class='mui-media-object' src=http://traveller.d4smarter.com"
    				+res.data.list[i].path+" id='" 
    				+res.data.list[i].id+"' data-preview-src='' data-preview-group='1'></li>";
    				
    			}
    		}
    	});
    	return str.val;
	}
	photo.deletImg=function(id){
    	$.ajax({
    		type:"POST",
    		url:"http://trveller.d4smarter.com/image/delete",
    		async:true,
    		dataType: 'json',
    		
    		data: {
    			id: id,
    		},
    		success:function(res){
    			alert("删除成功");
    		}
        });
   }
	photo.selectImg =function(){
		var str="";
        var img = document.myForm.img.files[0];

    var fm = new FormData();
    fm.append('image', img);
    $.ajax(
        {
            url: 'http://taveller.d4smarter.com/image/upload',
            type: 'POST',
            dataType: 'json',
            async:false,
            enctype: 'multipart/form-data',
            contentType: false, //禁止设置请求类型
            processData: false, //禁止jquery对DAta数据的处理,默认会处理
            //禁止的原因是,FormData已经帮我们做了处理 
            data: fm,
            success: function (result) {
                //测试是否成功
                //但需要你后端有返回值
                if(result.code==0){
                	str=result.data;
                //	alert("上传成功");
                }
                
            }
        }
    );
    return str;
}
}(mui, window.photo = {}));