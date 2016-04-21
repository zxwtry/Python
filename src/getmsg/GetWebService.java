package getmsg;

import java.rmi.RemoteException;
import java.util.Iterator;

import org.apache.axis2.AxisFault;
import org.json.JSONArray;
import org.json.JSONObject;

import getmsg.PublishProductServiceStub.GetAllProducts;
import getmsg.PublishProductServiceStub.GetListOfProducts;
import getmsg.PublishProductServiceStub.GetPublishModel;
import getmsg.PublishProductServiceStub.GetPublishString;

public class GetWebService {

	public static void main(String[] args) throws RemoteException {
		PublishProductServiceStub stub = new PublishProductServiceStub();
		GetPublishString getPublishString0 = new GetPublishString();
		getPublishString0.setName("zxwtry");
		String re = stub.getPublishString(getPublishString0).get_return();
		System.out.println(re);
		
		GetPublishModel getPublishModel2 = new GetPublishModel();
		getPublishModel2.setId(45);
		getPublishModel2.setName("zxwtry");
		int id = stub.getPublishModel(getPublishModel2).get_return().getId();
		String name = stub.getPublishModel(getPublishModel2).get_return().getName();
		getmsg.PublishProductServiceStub.SimpleModel model = stub.getPublishModel(getPublishModel2).get_return();
		
		// model.getOMElement(parentQName, factory)
		
		System.out.println(id+" ..... " + name);
		
		GetAllProducts getAllProducts0 = new GetAllProducts();
		getAllProducts0.setCipher("cipher");
		String string = stub.getAllProducts(getAllProducts0).get_return();
		System.out.println("AllProduct :  "+string);
		JSONArray jsonArray = new JSONArray(string);
		JSONObject jsonObject = null;
		Iterator<Object> iterator = jsonArray.iterator();
		while (iterator.hasNext()) {
			jsonObject = new JSONObject(iterator.next().toString());
			System.out.println("id : "+jsonObject.get("id").toString());
			System.out.println("allBuyers : "+jsonObject.get("allBuyers").toString());
			// System.out.println("allFiles : "+jsonObject.get("allFiles").toString());
			JSONArray jsonArray2 = new JSONArray(jsonObject.get("allFiles").toString());
			System.out.println(jsonArray2.length());
			for (int index = 0; index < jsonArray2.length(); index ++) {
				// 得到的是每一个商品图片的路径
				String string2 = jsonArray2.getString(index);
				System.out.println(string2);
			}
			System.out.println("productName : "+jsonObject.get("productName").toString());
			System.out.println("productPrice : "+jsonObject.get("productPrice").toString());
			System.out.println("sellerID : "+jsonObject.get("sellerID").toString());
		}
	}
}
