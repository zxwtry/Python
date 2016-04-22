package getmsgub;

import java.rmi.RemoteException;

import org.apache.axis2.AxisFault;
import org.json.JSONArray;
import org.json.JSONObject;

import getmsgub.PublishProductServiceStub.GetAllProducts;
import getmsgub.PublishProductServiceStub.GetListOfProducts;

import getmsgub.PublishProductServiceStub.Product;

public class GetWebServiice {

	public static void main(String[] args) throws RemoteException {
		// TODO Auto-generated method stub
		PublishProductServiceStub stub = new PublishProductServiceStub();
		GetAllProducts getAllProducts0 = new GetAllProducts();
		getAllProducts0.setCipher("AAA");
		String string = stub.getAllProducts(getAllProducts0).get_return();
		//System.out.println(string);
		JSONArray jsonArray = new JSONArray(string);
		int len1 = jsonArray.length();
		for (int i = 0; i < len1; i ++ ) {
			JSONObject jsonObject = new JSONObject(jsonArray.get(i).toString());
			System.out.println("id : "+new JSONArray(jsonObject.get("id").toString()).getInt(0));
			System.out.println("allBuyers : "+jsonObject.get("allBuyers").toString());
			// System.out.println("allFiles : "+jsonObject.get("allFiles").toString());
			JSONArray jsonArray2 = new JSONArray(jsonObject.get("allFiles").toString());
			// System.out.println(jsonArray2.length());
			for (int index = 0; index < jsonArray2.length(); index ++) {
				// 得到的是每一个商品图片的路径
				String string2 = jsonArray2.getString(index);
				JSONArray jsonArray3 = new JSONArray(string2);
				int len3 = jsonArray3.length();
				for (int j = 0; j < len3; j ++) {
					String path = jsonArray3.get(j).toString();
					System.out.println(path);
				}
			}
			System.out.println("productName : "+jsonObject.get("productName").toString());
			System.out.println("productPrice : "+jsonObject.get("productPrice").toString());
			System.out.println("sellerID : "+jsonObject.get("sellerID").toString());
		}
//		JSONArray jsonArray2 = new JSONArray("[\"11\"]");
//		System.out.println(jsonArray2.getInt(0));
	}

}
