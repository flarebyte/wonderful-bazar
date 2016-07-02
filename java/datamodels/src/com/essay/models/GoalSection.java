package com.essay.models;

import java.util.List;

public interface GoalSection extends Visitable{
	public SectionType getType();
	public GoalPriority getPriority();
	public List<Goal> getGoalList();
}
