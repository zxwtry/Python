/**
 * PublishProductServiceCallbackHandler.java
 *
 * This file was auto-generated from WSDL
 * by the Apache Axis2 version: 1.7.1  Built on : Feb 20, 2016 (10:01:29 GMT)
 */
package getmsg;


/**
 *  PublishProductServiceCallbackHandler Callback class, Users can extend this class and implement
 *  their own receiveResult and receiveError methods.
 */
public abstract class PublishProductServiceCallbackHandler {
    protected Object clientData;

    /**
     * User can pass in any object that needs to be accessed once the NonBlocking
     * Web service call is finished and appropriate method of this CallBack is called.
     * @param clientData Object mechanism by which the user can pass in user data
     * that will be avilable at the time this callback is called.
     */
    public PublishProductServiceCallbackHandler(Object clientData) {
        this.clientData = clientData;
    }

    /**
     * Please use this constructor if you don't want to set any clientData
     */
    public PublishProductServiceCallbackHandler() {
        this.clientData = null;
    }

    /**
     * Get the client data
     */
    public Object getClientData() {
        return clientData;
    }

    /**
     * auto generated Axis2 call back method for getPublishString method
     * override this method for handling normal response from getPublishString operation
     */
    public void receiveResultgetPublishString(
        getmsg.PublishProductServiceStub.GetPublishStringResponse result) {
    }

    /**
     * auto generated Axis2 Error handler
     * override this method for handling error response from getPublishString operation
     */
    public void receiveErrorgetPublishString(java.lang.Exception e) {
    }

    /**
     * auto generated Axis2 call back method for getPublishModel method
     * override this method for handling normal response from getPublishModel operation
     */
    public void receiveResultgetPublishModel(
        getmsg.PublishProductServiceStub.GetPublishModelResponse result) {
    }

    /**
     * auto generated Axis2 Error handler
     * override this method for handling error response from getPublishModel operation
     */
    public void receiveErrorgetPublishModel(java.lang.Exception e) {
    }
}
