package com.essay.models;

import java.util.List;

public interface Desire extends Visitable, Identifiable{
	public List<GoalSection> getGoalSectionList();
}
