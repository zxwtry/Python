package getmsg;

import java.rmi.RemoteException;

import org.apache.axis2.AxisFault;

import getmsg.PublishProductServiceStub.GetPublishString;

public class GetWebService {

	public static void main(String[] args) throws RemoteException {
		PublishProductServiceStub stub = new PublishProductServiceStub();
		GetPublishString getPublishString0 = new GetPublishString();
		getPublishString0.setName("zxwtry");
		String re = stub.getPublishString(getPublishString0).get_return();
		System.out.println(re);
	}

}
