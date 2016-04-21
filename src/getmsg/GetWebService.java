package getmsg;

import java.rmi.RemoteException;

import getmsg.PublishProductServiceStub.GetPublishModel;
import getmsg.PublishProductServiceStub.GetPublishModelResponse;
import getmsg.PublishProductServiceStub.GetPublishString;

public class GetWebService {

	public static void main(String[] args) throws RemoteException {
		PublishProductServiceStub stub = new PublishProductServiceStub();
		GetPublishString getPublishString0 = new GetPublishString();
		getPublishString0.setName("zxwtry");
		System.out.println(stub.getPublishString(getPublishString0).get_return());
		GetPublishModel getPublishModel2 = new GetPublishModel();
		getPublishModel2.setId(12);
		getPublishModel2.setName("zxwtry2");
		GetPublishModelResponse simpleModel = stub.getPublishModel(getPublishModel2);
		System.out.println(simpleModel.get_return().getId());
	}

}