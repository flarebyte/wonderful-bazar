package com.flarebyte.cm.trash.admin;

public interface User {
	public SocialNetworkIterator getSocialNetworks(String... options);

	public void joinSocialNetwork(SocialNetwork socialNetwork);

}
