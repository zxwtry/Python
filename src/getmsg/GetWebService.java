package getmsg;

import java.rmi.RemoteException;

import org.apache.axis2.AxisFault;

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
		System.out.println(string);
	}
	
}
